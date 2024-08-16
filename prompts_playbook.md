# Playbook

We gonna demo with the following two sample files.

---

## For `BudgetRequestSummary.json`

Try:
```
name and adress only
```

---

## For `California-Standard-Residential-Lease-Agreement-Sophia.json`

You can try the following prompts in turn:
```
1. Also hide "123 Maple Street", and ”Springfield, IL 62704" separately while having the original address

2. Also hide "123 Maple Street", and ”Springfield, IL 62704" separately

3. Keep the original address
```

- try 1
- try 1 -> 2 -> 3
- try 2
- try 2 -> 3
- try 2 -> 3 -> 1

### For example:

1. First user prompt:
    ```
    Also hide "123 Maple Street", and ”Springfield, IL 62704" separately
    ```

    You will get the following result:
    ```
    ============================
    Turn 1:
    User input: Also hide "123 Maple Street", and ”Springfield, IL 62704" separately
    - Name: Olivia Johnson
    - Name: Noah Davis
    - Address: 123 Maple Street, Springfield, IL 62704
    - Address: 123 Maple Street
    - Address: Springfield, IL 62704
    - Name: James Taylor
    - Name: Isabella Miller
    ============================
    Goodbye :)

    ```

2. There's a chance it didn't work well, second prompt:
    ```
    Keep the original address
    ```

    You will get the following result:
    ```
    ============================
    Turn 1:
    User input: Also hide "123 Maple Street", and ”Springfield, IL 62704" separately
    - Name: Olivia Johnson
    - Name: Noah Davis
    - Address: 123 Maple Street
    - Address: Springfield, IL 62704
    - Name: James Taylor
    - Name: Isabella Miller
    ============================
    Turn 2:
    User input: Keep the original address
    - Name: Olivia Johnson
    - Name: Noah Davis
    - Address: 123 Maple Street, Springfield, IL 62704
    - Address: 123 Maple Street
    - Address: Springfield, IL 62704
    - Name: James Taylor
    - Name: Isabella Miller
    ============================
    Goodbye :)
    ```

3. Third prompt:
    ```
    Also hide "123 Maple Street", and ”Springfield, IL 62704" separately while having the original address
    ```
    You will get the following result:
    ```
    ============================
    Turn 1:
    User input: Also hide "123 Maple Street", and ”Springfield, IL 62704" separately
    - Name: Olivia Johnson
    - Name: Noah Davis
    - Address: 123 Maple Street
    - Address: Springfield, IL 62704
    - Name: James Taylor
    - Name: Isabella Miller
    ============================
    Turn 2:
    User input: Keep the original address
    - Name: Olivia Johnson
    - Name: Noah Davis
    - Address: 123 Maple Street, Springfield, IL 62704
    - Name: James Taylor
    - Name: Isabella Miller
    ============================
    Turn 3:
    User input: Also hide "123 Maple Street", and ”Springfield, IL 62704" separately while having the original address
    - Name: Olivia Johnson
    - Name: Noah Davis
    - Address: 123 Maple Street, Springfield, IL 62704
    - Address: 123 Maple Street
    - Address: Springfield, IL 62704
    ...
    - Name: James Taylor
    - Name: Isabella Miller
    ============================
    Goodbye :)
    ```