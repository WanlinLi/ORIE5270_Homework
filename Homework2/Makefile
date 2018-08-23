cover:

	make lint

	make cover_tests



lint: 

	flake8 --max-line-length=100 tree_folder test_folder
 


cover_tests:

	py.test -s  --cov-config .coveragerc --cov tree_folder \

	--no-cov-on-fail \

	--cov-fail-under=90 \

	test_folder
