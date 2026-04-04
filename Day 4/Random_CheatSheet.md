# RANDOM CHEATSHEET IN PYTHON


| Function           | Input Type                     | Output Type     | Description                                              | Notes                                      | Example                          |
|-------------------|--------------------------------|------------------|----------------------------------------------------------|--------------------------------------------|----------------------------------|
| random.shuffle    | list (mutable)                | None             | Shuffles elements in-place                               | Modifies original list                     | shuffle([1,2,3]) -> [2,1,3]       |
| random.choice     | sequence (list, str, tuple)   | single element   | Returns random element                                   | Does not modify input                      | choice([1,2,3]) -> 2              |
| random.choices    | sequence, k=int               | list             | Returns k random elements (with replacement)             | Duplicates allowed                         | choices([1,2,3], k=2) -> [1,1]    |
| random.sample     | sequence, k=int               | list             | Returns k unique elements (no replacement)               | No duplicates                              | sample([1,2,3], 2) -> [1,3]       |
| random.randint    | int, int                      | int              | Returns int where a ≤ x ≤ b                              | Inclusive range                            | randint(1,5) -> 3                 |
| random.random     | None                          | float            | Returns float where 0.0 ≤ x < 1.0                        | Start inclusive, end exclusive             | random() -> 0.734                 |
| random.uniform    | float, float                  | float            | Returns float where a ≤ x ≤ b                            | Typically inclusive of both ends           | uniform(1,5) -> 3.42              |

