import {Bard} from "bard-ai";

function getRecommendations() {
    
    const productInput = document.getElementById('productInput').value;
    const recommendationsDiv = document.getElementById('recommendations');

    const BARD_API_KEY = "cQgD4wdeVXhSDyYfvmHKNkBfiukGOyI73brZ7vKOfvuEo727ZlMU_SF01xdbad1bWzJ0vg";
    //const Bard = require('bard-ai');
    const bard = new Bard(BARD_API_KEY);

    // Replace the placeholder URL with your actual backend API endpoint
    //const apiEndpoint = '/api/recommendations';

    // Make an API call to the backend server with the user input
    try {
        //const response = await fetch(`${apiEndpoint}?product=${encodeURIComponent(productInput)}`);
        
        const response = bard.ask(productInput).then(() => {
            console.log("RESPONSE: ", response);
        });
        

        // Check if the response status is OK (status code 200)
        if (response.ok) {
            // const data = await response.json();

            // Update the #recommendations element with the fetched data
            // if (data && data.length > 0) {
            //     const productsHtml = data.map(product => `<p>${product}</p>`).join('');
            //     recommendationsDiv.innerHTML = productsHtml;
            // } else {
            //     recommendationsDiv.innerHTML = '<p>No recommendations found.</p>';
            // }
        }
    } catch (error) {
        // Handle network errors or other exceptions
        console.error('Error fetching recommendations:', error);
        recommendationsDiv.innerHTML = '<p>Error fetching recommendations. Please try again later.</p>';
    }
}