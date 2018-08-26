cover:

	make cover_tests

lint: 

	flake8 --max-line-length=100 find_circle_folder test_folder

cover_tests:

	py.test -s  --cov-config .coveragerc --cov find_circle_folder \
	--no-cov-on-fail \
	--cov-fail-under=90 \
	test_folder
