# featureRequests
Allow users to request a new feature

### create requests table in Database
'''
CREATE TABLE requests (
  id int NOT NULL AUTO_INCREMENT,
  title varchar(255) NOT NULL,
  description text NOT NULL,
  client varchar(255) NOT NULL,
  priority int NOT NULL,
  target_date date NOT NULL,
  product_area varchar(255) NOT NULL,
  PRIMARY KEY (id)
);
'''
