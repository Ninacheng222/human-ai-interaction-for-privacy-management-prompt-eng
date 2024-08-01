from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() # load API key

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)

def chat_with_gpt(messages):
    completion = client.chat.completions.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=messages
    )
    return completion.choices[0].message.content

def init_conversation(ocr_input):

    input_doc = '<document>'+ocr_input['img_string']+'</document>'
    # print(f'{input_doc=}')

    input_system = """You are now a strict sensitive information protection officer. You must protect customer privacy and ensure that sensitive information in documents is not leaked. Here are some categories of personal data: Name, Phone Number, ID Number, Social Security Number (SSN), Email Address, Address, Date of Birth, Gender, Nationality, Passport Number, Bank Account Number, Driver's License Number, Occupation, Health Information, Marital Status, Income or Wage. These types of data (including but not limited to) are usually considered sensitive and need to be properly protected to prevent unauthorized access and use."""

    positive_examples = """For example, here is a sample document that contains sensitive information:

    <document>Dear Loan Department Manager, My name is Zhang Xiaoming, currently residing at Guangfu South Road, Xinyi District, Taipei City. I am hereby submitting a loan application to your esteemed bank. The purpose of this letter is to request a loan to support my personal financial needs. I plan to use the loan funds for home renovation to enhance the comfort of my residence. As a loan applicant, I am willing to comply with all the terms and conditions set by your bank. I understand that the loan application may require the submission of additional documentation, and I am ready to cooperate and complete these procedures. Below is a summary of my personal profile and financial status: Personal Profile: I am an IT professional with over five years of experience working at a renowned technology company. I have a good credit record and repayment capability. Income Situation: My primary source of income is my monthly salary, which provides a stable income sufficient to support the repayment plan. Financial Status: My financial status is stable, and I have several years of financial records that can demonstrate my repayment ability. I sincerely hope that your bank will approve my loan application, allowing me to achieve the aforementioned financial goals. I am willing to provide further information or documents at any time to assist in the review of my application. Sincerely, Zhang Xiaoming July 2, 2024</document>

    You need to list out the sensitive information like this:
    "- Name: Zhang Xiaoming
    - Address: Guangfu South Road, Xinyi District, Taipei City"
    No explanation is needed.
    """

    input_text = """Here is a document. Identify the text containing sensitive information and list it with bullet points, like this: "-Name: Amy, -SSN: 123456789." No explanation needed:"""

    # initialize the conversation history
    conversation_history = [
        {"role": "system", "content": input_system},  # system prompt
        {"role": "system", "content": positive_examples},
        {"role": "user", "content": input_text},
        {"role": "user", "content": input_doc} # first input doc that generated from OCR
    ]
    response_from_gpt = chat_with_gpt(conversation_history)
    print("\nGPT:\n", response_from_gpt, "\n")

    conversation_history.append({"role": "assistant", "content": response_from_gpt})

    return conversation_history, response_from_gpt


def continued_conversation(conversation_history, user_input):

    # customize user input to eventual prompts
    # ======================================= #
    #             customize here              #
    # ======================================= #

    # add user input prompts to conversation history
    conversation_history.append({"role": "user", "content": user_input})
    # print(f'{conversation_history=}')

    # get response from ChatGPT
    response_from_gpt = chat_with_gpt(conversation_history)
    
    # add ChatGPT response to conversation history
    conversation_history.append({"role": "assistant", "content": response_from_gpt}) # role is assistant
    
    # print the response
    print("\n============================")
    print("User input:", user_input)
    print("\nGPT:\n", response_from_gpt, "\n")

    return conversation_history, response_from_gpt


def post_processing(response_from_gpt, ocr_input):

    masks = []

    for i in response_from_gpt.split('\n'):

        words = i.split('- ')[-1].split(': ')[-1]
        print(words)

        for i in range(len(ocr_input['ocr_result'])):
            if words in ocr_input['ocr_result'][i]['text']:
                print(ocr_input['ocr_result'][i]['bbox'])

                masks.append({"top_left": [ocr_input['ocr_result'][i]['bbox'][0], ocr_input['ocr_result'][i]['bbox'][3]],
                     "bottom_right": [ocr_input['ocr_result'][i]['bbox'][2], ocr_input['ocr_result'][i]['bbox'][1]]})
    
    return masks


def prompt(input_json):

    if input_json['conversion_type'] == 'first':

        conversation_history, gpt_response = init_conversation(input_json['ocr_json'])
        masks = post_processing(gpt_response, input_json['ocr_json'])

    elif input_json['conversion_type'] == 'continued':

        conversation_history, gpt_response = continued_conversation(input_json['conversation_history'], input_json['user_input'])
        masks = post_processing(gpt_response, input_json['ocr_json'])

    return [
        {
            "conversion_type": input_json['conversion_type'],
            "conversation_history": conversation_history,
            "masks": masks
        }
    ]
