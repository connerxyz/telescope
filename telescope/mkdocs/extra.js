// For removing the class names added by Pandas dataframes rendered as HTML
var elements = document.getElementsByClassName("dataframe");
while(elements.length > 0){
  elements[0].removeAttribute("class");
}
