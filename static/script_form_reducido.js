/**
* Retrieves input data from a form and returns it as a JSON object.
* @param {HTMLFormControlsCollection} elements the form elements
* @return {Object} form data as an object literal
*/
const formToJSON = (elements) =>
[].reduce.call(
elements,
(data, element) => {
data[element.name] = element.value;
return data;
},
{},
);
const handleFormSubmit = (event) => {
// Stop the form from submitting since we’re handling that with AJAX.
event.preventDefault();
// Call our function to get the form data.
const data = formToJSON(form.elements);
// Demo only: print the form data onscreen as a formatted JSON object.
const dataContainer = document.getElementsByClassName('results__display')[0];
// Use `JSON.stringify()` to make the output valid, human-readable JSON.
dataContainer.textContent = JSON.stringify(data, null, ' ');
// ...this is where we’d actually do something with the form data...
};
const form = document.getElementsByClassName('contact-form')[0];
form.addEventListener('submit', handleFormSubmit);

// This is the function that is called on each element of the array.
const reducerFunction = (data, element) => {
// Add the current field to the object.
data[element.name] = element.value;
// For the demo only: show each step in the reducer’s progress.
console.log(JSON.stringify(data));
return data;
};