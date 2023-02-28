# ArrayWork
  
Module for work with arrays and tables  

*Read this in other languages: [English](Manual_ArrayWork.md), [Español](Manual_ArrayWork.es.md).*
  
![banner](imgs/Banner_ArrayWork.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



## Description of the commands

### Find element position in table
  
Find the position of the element in a table. It must be an Array of arrays
|Parameters|Description|example|
| --- | --- | --- |
|Value to search|Value to search in the table|Value to search|
|Where to search|Where to search the value|[[1,2,3],[4,5,6],[7,8,9]]|
|Name of the variable where to store the position|Name of the variable where to store the positions of the element|Result|

### Delete data in array
  
Delete data in array by value or position
|Parameters|Description|example|
| --- | --- | --- |
|Array|Array where the data will be deleted|{array}|
|Option|Option to delete data|By Position|
|Value or Position to delete |Value or position to delete from the array|test|
|Assign result to variable |Variable where the result will be stored|test|

### Add data in array
  
Add an array data, you can indicate position if it is a single value
|Parameters|Description|example|
| --- | --- | --- |
|Array|Array where the data will be added|{array}|
|Position|Position where the data will be added|{posicion}|
|Value to add |Value to add in the array|test|
|Add like number|Add the value as a number|test|
|Assign result to variable|Assign the result of the execution to a variable|variable|

### Filter
  
Compares an array with a data and returns an array with the elements that meet the condition.
|Parameters|Description|example|
| --- | --- | --- |
|Array|Array to filter|{array}|
|Condition|Condition to evaluate|Equal to|
|Data|Data to compare|{data}|
|Assign result to variable |Assign result to variable|test|

### Count elements
  
Return a number of array elements
|Parameters|Description|example|
| --- | --- | --- |
|Array|Array to count|{array}|
|Assign result to variable |Variable where the result will be stored|test|

