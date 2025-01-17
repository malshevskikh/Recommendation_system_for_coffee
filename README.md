# Recommendation_system_for_coffee
<!-- UNIVERSITY LOGO -->
<div align="center">
  <a href="https://bmstu.ru">
    <img src="https://user-images.githubusercontent.com/67475107/225371733-8fd6f639-bf62-49bd-866c-4e08116fa20c.png" alt="University logo" height="200">
  </a>
  
  Developed by Maxim Alshevskikh (<a href="https://www.linkedin.com/in/maxim-alshevskikh-b473b42b3/">LinkedIn</a>)
  <br/>
</div>

<h2>Lab tasks on the subject "Artificial Intelligence Systems":</h2>
<ul>
  <li>Select a topic for lab</li>
  <li>Create a dataset with a minimum of 25 objects</li>
  <li>Select the attributes by which objects will be compared</li>
  <ul>
      <li>1 binary attribute</li>
      <li>2 numerical attributes</li>
      <li>1 non-numeric attribute</li>
  </ul>
  <li>Create a hierarchy (classification) of objects of the selected subject, in the form of a tree with a minimum height of 4</li>
  <li>Select proximity measures for objects</li>
  <li>Implement a content-oriented recommendation system</li>
  <li>Implement filters by object attributes. Formation of data sampling step by step</li>
  <li>Develop questions and scenarios for dialogue systems</li>
  <li>Implementation of a dialogue system that interacts with the user in natural language (Russian) within a given topic with a limited set of conversation scenarios</li>
</ul>

<h2>Задачи лабораторной работы по предмету "Системы Искусственного Интеллекта":</h2>
<ul>
  <li>Выбрать тематику для лабораторной работы</li>
  <li>Создать/найти датасет с минимально колличеством в 25 объектов</li>
  <li>Выбрать признаки, по которым объекты будут сраниваиться</li>
  <ul>
      <li>1 бинарный признак</li>
      <li>2 числовых признака</li>
      <li>1 не приводимый к числовому признак</li>
  </ul>
  <li>Создать иерархию (классификацию) объектов выбранной тематики, в виде дерева с минимальной высотой 4</li>
  <li>Выбрать меры близости для объектов</li>
  <li>Создать контент-ориентированную рекомендательную систему</li>
  <li>Создать фильтры по признакам объектов. Формирование выборки данных поэтапно</li>
  <li>Создать вопросы и сценарии для диалоговой системы</li>
  <li>Создать диалоговую систему, которая взаимодействует на естественном языке (русском) в рамках заданной тематики с ограниченным набором сценариев беседы</li>
</ul>


<h2>Results:</h2>
<h3>1.Topic - Coffee</h3>
<h3>2.Dataset in russian(in coffee_dataset.csv)</h3>
<h3>3.Coffee attributes:</h3>
<ul>
    <li>Coffee variety (сорт кофе)</li>
    <li>Package weight (in grams) (вес упаковки с кофе в граммах)</li>
    <li>Roast level (light, medium, dark) (степень прожарки свтелая, средняя, темная)</li>
    <li>Country of coffee growing (страна произростания кофе)</li>
    <li>Сoffee taste/flavors/aromas (вкусы кофе)</li>
</ul>
<h3>4.Hierarchy (classification) of for coffee taste:</h3>
<h4>Pie chart of taste (in russian):</h4>

![taste1](https://github.com/user-attachments/assets/9e4984a1-902b-401b-a824-0233f5d76a2c)
<h4>Pie chart of taste (in english):</h4>

<img width="793" alt="taste2" src="https://github.com/user-attachments/assets/e8a5e590-a2a3-40e3-8463-a055a09c5ab6" />
<h4>Classification tree (in russian):</h4>

<img width="1183" alt="tree1" src="https://github.com/user-attachments/assets/d45400a0-6470-4a38-832b-827b4c6c73b0" />

<h5>Part №1:</h5>

<img width="1283" alt="tree_part1" src="https://github.com/user-attachments/assets/64427a03-cc68-4d44-a0b2-fbc0e37469bb" />

<h5>Part №2:</h5>

<img width="1179" alt="tree_part2" src="https://github.com/user-attachments/assets/ee859b14-0fda-47d5-8340-738187b4767f" />



<h3>5.Measures of proximity::</h3>
<ul>
    <li>Number of grams in a package of coffee</li>
    <li>Degree of roasting</li>
    <li>Geographical location of coffee growing, comparison of how close they are to the countries of growth</li>
    ![wporld](https://github.com/user-attachments/assets/15e31c3b-4df9-4dce-851b-e42b7f06c4ce)
    <li>Measure of proximity by tree – how close/far two objects are from each other. It is also associative</li>
</ul>
