# Сheck Your Code Against the Following Points

## Don`t Repeat Yourself

1. Create functions when needed.

Good example:

```python
def check_temperature(temperature: int) -> int:
    if temperature <= 10:
        temperature = 10

    return temperature

morning_temperature = 9
evening_temperature = 22

print(check_temperature(morning_temperature))  # 10
print(check_temperature(evening_temperature)) # 22
```

Bad example:

```python
morning_temperature = 9
evening_temperature = 22

if morning_temperature <= 10:
    morning_temperature = 10

if evening_temperature <= 10:
    evening_temperature = 10
```

2. Use the `for` loops.

Good example:

```python
home_chores = {
    "cleaning": "not done",
    "ironing_shirts": "not done"
}

to_do_list = ["cleaning", "ironing_shirts"]

for home_chore in to_do_list:
    if home_chore in home_chores:
        home_chores[home_chore] = "done"
```

Bad example:

```python
home_chores = {
    "cleaning": "not done",
    "ironing_shirts": "not done"
}

if "cleaning" in home_chores:
    home_chores["cleaning"] = "done"
    
if "ironing_shirts" in home_chores:
    home_chores["ironing_shirts"] = "done"
```

3. DRY while creating class instances:

Good example:

```python
citizens = {
    "names": ["Dima", "Dania"], 
    "surnames": ["Smith", "Green"]
}

citizens_list = []


class Citizen:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname


for i in range(len(citizens)):
    citizens_list.append(Citizen(name=citizens["names"][i], surname=citizens["surnames"][i]))
```

Bad example:

```python
citizens = {
    "names": ["Dima", "Dania"], 
    "surnames": ["Smith", "Green"]
}

citizens_list = []


class Citizen:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname


citizens_list.append(Citizen(name=citizens["names"][0], surname=citizens["surnames"][0]))
citizens_list.append(Citizen(name=citizens["names"][1], surname=citizens["surnames"][1]))
```

## Code Style

1. Make sure you use the double quotes everywhere.

Good example:

```python
greetings = "Hi, mate!"
```

Bad example:

```python
greetings = 'Hi, mate!'
```

2. Use descriptive and correct variable names.

Good example:

```python
def get_full_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}"
```

Bad example:

```python
def get_full_name(x: str, y: str) -> str:
    return f'{x} {y}'
```

3. Use annotation, it is a good practice.

Good example:

```python
def multiply_by_2(number: int) -> int:
    return number * 2
```

Bad example:

```python
def multiply_by_2(number):
    return number * 2
```

4. Use the `snake_case`.

Good example:

```python
knights_preparation = "we are preparing"
```

Bad examples:

```python
knightsPreparation = "we are preparing"
KnightsPreparation = "we are preparing"
```

5. Separate your code into different modules and/or packages. 
It is a good idea when you are working with a big project.

## Clean Code

Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.
