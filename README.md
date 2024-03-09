Odoo Forked
----
This repository contains feature extensions for mainly Odoo:16.0.0.

Running in Docker
-------------------------
- To create and run the odoo-web and odoo-db services execute below
  ```
      docker-compose up -d
  ```
- For first-time odoo inits execute below
  ```
      docker exec odoo-web bash -c "./etc/odoo/odoo_init.sh"
      docker restart odoo-web
  ```
  
Testing
-----------------
- Execute the below command
  ```
      python -m ...addons.od_product.tests.test_extended_product_template
  ```
  
  
Requirements
----------------
- See the [here](https://hub.docker.com/_/odoo/)
