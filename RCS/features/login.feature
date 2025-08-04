Feature: Validation in Site Management page
    This test verifies the functionality in Site Management page

# Scenario Outline: Verify StatusOverView Section using pageObject model 
#      Given I launch the url
#      And I login as <ROLE> 
#      When I navigate to Site Management page
#      Then I verify whether Status overview section is displayed   
     
#     Examples: 
#             |   ROLE                |
#             | propertymanager       |

# Scenario Outline: Verify User Login using external pageObject model
#      Given I launch the url 
#      And I login as <ROLE> with external POM
#      When I navigate to Site Management page 

#     Examples: 
#             |   ROLE                |
#             | facilitymanager       |    

Scenario Outline: Verify Search functionality in Device Management page 
     Given I launch the url 
     And I login as <ROLE> 
     When I navigate to Device Management page 
     Then I verify whether Search functionality is working fine

    Examples: 
            |   ROLE                |
            | facilitymanager       |
       
       