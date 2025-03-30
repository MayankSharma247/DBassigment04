# DBassigment04

Prerequisites
Ensure that the following tools are installed:

Ansible (for automation)
MySQL (for the database)
Flyway (for database migrations)
Python (for schema validation scripts)


Start MySQL with Ansible (up.yaml)

To deploy the MySQL container and apply Flyway migrations, run:

ansible-playbook ansible/up.yaml

Start the MySQL container.
Wait for MySQL to be ready.
Run Flyway to apply database migrations.

2. Running the Tests

After running the up.yaml playbook, execute the tests to verify the schema updates:

python tests/dbtests.py


Check if the subscribers table and the subscription_date column exist.
Insert a test subscriber and verify that the subscription_date column is automatically populated.
3. Shutting Down the MySQL Container (down.yaml)

Once you're done with the project, run:

ansible-playbook ansible/down.yaml


Shut down the MySQL container.
Save the state of the database for the next session.
Example Output
When running the tests, you should see an output like this:

