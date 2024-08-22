# Playbook

We gonna demo with the following two sample files.

---

## For `BudgetRequestSummary.json`

Try:
```
name and institution only
```

---

## For `California-Standard-Residential-Lease-Agreement-Sophia.json`

Try:
```
also add two-line format address aditionally
```

You will get the following result:
```
============================
Turn 1:
User input: also add two-line format address aditionally
- Name: Olivia Johnson
- Name: Noah Davis
- Address: 123 Maple Street, Springfield, IL 62704
- Address: 123 Maple Street
- Address: Springfield, IL 62704
- Name: James Taylor
- Name: Isabella Miller
============================
```

The back-up prompts you can try in turn:
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