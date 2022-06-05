pytest -v -m "sanity" --html=./Reports/sanity_report.html testCases/  --browser chrome
rem pytest -v -m "regression" --html=./Reports/regression_report.html testCases/  --browser chrome
rem pytest -v -m "sanity and regression" --html=./Reports/sanity_and_regression_report.html testCases/  --browser chrome
rem pytest -v -m "sanity or regression" --html=./Reports/sanit_or_regression_report.html testCases/  --browser chrome


rem pytest -v -m "sanity" --html=./Reports/sanity_report.html testCases/  --browser firefox
rem pytest -v  -m "regression" --html=./Reports/regression_report.html testCases/  --browser firefox
rem pytest -v -m "sanity and regression" --html=./Reports/sanity_and_regression_report.html testCases/  --browser firefox
rem pytest -v -m "sanity or regression" --html=./Reports/sanit_or_regression_report.html testCases/  --browser firefox

