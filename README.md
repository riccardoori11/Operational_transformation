Introduction:

A sample of a how a Operational Transformation would be created in Python. Needs a lot of revising and is only inteded to get a picture on this complex algorithm.

What is Operational Transformation ?

OT enables multiple users to make concurrent changes to a shared document and ensures that all replicas of the document converge to the same state. It handles conflicts and maintains intention-preservation, meaning each user’s change is reflected as they intended.
- Example:
    - Insert: `Insert(5, "A")` means "insert 'A' at position 5.
    - Delete: `Delete(5, 2)` means "delete 2 characters starting at position 5.

All this algorithm is saying is that if Op2 makes a change, Op1 can't use the same input and thus must make adjustments to fit with their original intention whilst taking into account op2's transformation

Different relationships :

- Insertion - Insertion
- Insertion - Deletion
- Deletion - Deletion


Sources:
https://github.com/kingdion/wordsmiths/blob/master/wordsmiths/ot.py
https://fitzgen.com/2011/04/05/operational-transformation-operations.html
High Latency, Low-Bandwidth Windowing in the Jupiter Collaboration System by David A. Nichols, Pavel Curtis, Michael Dixon, and John Lamping.