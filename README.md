## Instructions

Build a command-line program for a pet marketplace that reads sitter review data from a CSV and outputs a ranked list of sitters.

Calculate Profile Score from the sitter’s name and Ratings Score from stay reviews.

Compute Search Score as a weighted average of Profile and Ratings Scores, adjusting weights based on the number of stays.

Output sitters.csv with columns: email, name, profile_score, ratings_score, search_score, sorted by Search Score descending.

Write tests to verify scoring calculations and sorting logic.

Include a README with setup instructions and a discussion on production implementation or infrastructure choices.



## Presentation
Rebuilt pet_market_place search ranking algorithm using Python. Computes Profile Score, Ratings Score, and Search Score for sitters based on input CSV data.  
Includes both a backend (OO/domain-driven) and analytical (SQL/pandas/ETL) approach. Both processes create a new CSV file with the same content.  
The backend approach output is sitters.csv, and the data approach output is sitters_data_approach.csv. Both output files contain the same results.

In the backend, I built three layers:  
- **Domain layer:** represents the business objects like Users, Sitters, Owners, and Reviews.  
- **Database layer:** acts as the in-memory storage where all the information is persisted.  
- **Service layer:** connects the two and applies business logic to manage interactions between domain objects and the database.  

For a production setup, I would use Docker to containerize the application and make deployment easier and more consistent across environments. 


## Testing 
In the backend, both generic and unit tests were implemented (located inside the tests folders of the database, domain, and service modules).
Not all components were fully tested due to time constraints.

For the data approach, the ETL process was not directly tested for the same reason, but examples of the types of analytical tests that would normally be included (such as tests for primary keys, null values, data formats, and value consistency) can be found in the tests folder under the data_approach directory.

Finally, a visual comparison test was performed to verify that both the backend and data approaches generate the exact same output CSV file.



---

## Installation

```bash
# 1. Go to the project folder
cd pet_marked_place   # navigate to the directory containing this README

# 2. Create a virtual environment (safer with copies)
python3.12 -m venv --copies venv

# 3. Activate the virtual environment
source venv/bin/activate    # Mac/Linux

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the app
python -m python_code.app.main

# 6. Run tests
python -m pytest
```

---

