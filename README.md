<h1 align="center">Bod's Space Adventure Game - Project Portfolio 3</h1>

## - By Joe Playdon
 
### [View the live project here](https://bodthegod.github.io/codequiz/) #
### [View the repository here](https://bod-space-adventure.herokuapp.com/) #

# Table of Contents:
1. [About my game](#about-my-game)
    1. [How to Play](#how-to-play)
    2. [Returning and Frequent Visitor Goals](#instructions)
2. [Features](#features)
    1. [Existing Features](#existing-features)
    2. [Future Features](#future-features)
    3. [Data Model](#data-model)
	4. [Wireframes](#wireframes)
    5. [Screenshots of Features](#screenshots-and-features-within-website)
3. [Languages and Resources](#languages-used)
4. [Testing](#testing)
    1. [Python Validator Results](#python-results)
    2. [Validator Testing](#validator-testing)
    3. [Manual Testing](#manual-testing)
5. [Bugs and fixes](#known-bugs)
6. [Deployment](#deployment)
    1. [Heroku](#heroku)
7. [Credits](#credits)
    

![Website Designs]()</h2>

### About my game

This is my command line interface adventure game that allows for the user to make decisions to change the storyline. 

This game is run on the Code Institute mock terminal on heroku.


## How to play

-   ### Instructions

    1. The player is given the option to read a guide on how to play the game, and given basic information about the lore in the game.
    2. To play the game, it is very simple. You as the user are given the ability to choose yes or no, and when presented missions you can select 1, 2 or 3.
    3. The player is randomly selected a weapon at the start of the game, and there are many opportunities for the player to decide what they do, which has impact on the storyline.

-   ### Features

    -   #### Existing Features

        -   
        

    -   #### Future Features

        -   

    -   #### Data Model

        -   

    *   ### Wireframes
        
    -   I have used [Balsamiq Wireframes](https://balsamiq.com/) as my desired wireframing tool for this quiz, as it is very easy to use. However, due to these being wireframes, the final image of the quiz may be depicted differently yet these are base guidelines of my website, and the image I would like to achieve. Here I have created Start button, Game guide, Game area and Final score screen wireframes. As this quiz maintains consistency of look on both mobile and desktop views, the wireframes are the same.    

    -   Start Button Desktop and Mobile Wireframe - [View](/wireframes/Start-btn-wf.png)

    -   Guide Area Desktop and Mobile Wireframe - [View](/wireframes/Guide-wf.png)

    -   Game Area Desktop and Mobile Wireframe - [View](/wireframes/Game-area-wf.png)

    -   Final Score Desktop and Mobile Wireframe - [View](/wireframes/Final-score-wf.png)


### Screenshots and features within website
#### **(I have provided screenshots via links to make the screenshots section more readable)**
####   All Sections
-   [Start Button](/readmeimages/start-btn-ss.png) This screenshot shows the landing page of my quiz website, and this is the page a user will see every time they load up the site. This is a simple but effective way to catch the user's attention, as there is only one single button to be viewed, on an eye catching background. This button, upon hover- displays a gradient green to black background within the button, and a white box shadow, white text and white border to emphasise the user interaction. Once this button is clicked, it will display the guide box for the user to read and understand how to play the game. 
    
-   [Guide Box](/readmeimages/guide-box-ss.png) This screenshot shows the guide box- as stated above, this box is displayed once the start button is clicked. This guide shows a list of three to keep the user interested and to keep the game simple. The guide box consists of two buttons, a quit game and continue game button. When the quit game button is pressed, it takes the user back to the start button and when the continue game button is pressed, the game area box is presented and the game starts.
    
-   [Game Area](/readmeimages/game-box-ss.png) This portion of the website is the main part that uses JavaScript, and this consists of the game title, time remaining counter, question display, answer display, progress bar on desktop, question counter and finally the next button. Here, the time remaining counter is displayed via JavaScript and counts from 5 down to 0, and when a question is selected, the timer and progress bar pauses, the next button is displayed and the answer selections are muted to lock in the answer the user has chosen. All of the data within this section is stored within the qdata JavaScript file that I have created.

-   [Game Area Active](/readmeimages/game-box-active-ss.png) In this screenshot it shows the active status of the answers. If the time runs out on the counter then the correct answer is displayed to the user with green gradient background- without a tick next to it to indicate the user has not chosen the correct answer. When the correct answer is selected, the tick is displayed. On the contrary, when a user selects the incorrect answer a red gradient background is displayed on the answer they have chosen. When the next button is clicked, it displays the next question from the qdata file, defined by qnumber.
    
-   [Final Score Box](/readmeimages/final-score-ss.png) Finally, the final score box is displayed after the 10th question is answered and the next button is clicked. This section is very simple but displays a couple icons from FontAwesome, these being two cakes and a checkered flag to show the user is finished. Furthermore, the score the user achieved throughout the quiz is displayed at the end, and mutliple different messages are shown regarding the score they got. There are also two buttons at the end being the start again button and the quit game button. If the start again button is selected then the quiz restarts from question one and the counter is set to go again. If the quit game button is selected then the user is taken back to the start button.
   

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)

-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language)


### Resources Used


-   I have used the W3 [HTML](https://validator.w3.org/#validate_by_input) and [CSS](https://jigsaw.w3.org/css-validator/#validate_by_input) validator, the [JavaScript](https://jshint.com/) validator and occasionally the [W3Schools](https://www.w3schools.com/) resources when I had an issues.

-   For my box shadows and box border radius, I used [BoxShadowGenerator](https://html-css-js.com/css/generator/box-shadow/)

-   I used [1stwebdesigner](https://1stwebdesigner.com/15-css-background-effects/) For help with the gradient animation background.

-   For testing my website on different screen sizes, I used Google Chrome Dev Tools.

-   For media query info, I used [W3Schools](https://www.w3schools.com/css/css_rwd_mediaqueries.asp)

-   For styling inspiration, I used [ColorMind](http://colormind.io/bootstrap/)

-   For font styles, I used [Google Fonts](https://fonts.google.com/)

-   Colours were all checked with [Contrast Grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23FFFFFF%2C%20White%0D%0A%23F2F2F2%0D%0A%23DDDDDD%0D%0A%23CCCCCC%0D%0A%23888888%0D%0A%23404040%2C%20Charcoal%0D%0A%23000000%2C%20Black%0D%0A%232F78C5%2C%20Effective%20on%20Extremes%0D%0A%230F60B6%2C%20Effective%20on%20Lights%0D%0A%23398EEA%2C%20Ineffective%0D%0A&es-color-form__tile-size=compact&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp)

-   Icons within the answer selection boxes and final score box were from [Font Awesome](https://fontawesome.com/)

-   To create the favicons I used [Favicon.io](https://favicon.io/favicon-generator/)


### Frameworks, Libraries & Programs Used

1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the fonts into the style.css file which is used throughout the whole project (maintains a certain style).
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on The final score box for the finish icons and the time icon within the game area, and tick and cross icons.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub, this was used throughout the development of the website
    and was essential.
1. [GitHub:](https://github.com/)
    - GitHub was used to store the projects code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](/wireframes/) during the design process.

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project. In addition to this, I used Chrome Dev tools very often to play around with the code and test when I was having issues. I found this was extremely important when troubleshooting issues- as I could change the code and see the changes live, instead of having to save the file and force refresh (If I changed the CSS code). I had also used the console and console.log feature within javascript to test wether the programming was functioning as intended, which was very helpful.

The use of chrome dev tools allowed me to play around with the breakpoints for different screen sizes, and helped me achieve the look I desire for on smaller screen sizes.

## Python Results

-   [W3C Markup Validator](https://validator.w3.org/)
-   [index.html Results](/readmeimages/html-validation.png)



### Validator Testing

-   

### Manual Testing

-    

### Known Bugs

-   

## Deployment

### Heroku

This project was deployed using Code Institute's mock terminal for Heroku

- Steps for deployment
    - Fork or clone this repository
    - Create a new Heroku app
    - Set the buildpacks to Python and NodeJS in that order
    - Link the Heroku app to the repo
    - Click on Deploy



## Credits

-   For information regarding the timer, credits to [educative.io](https://www.educative.io/answers/how-to-create-a-countdown-timer-using-javascript)
-   For inspiration of the design and features of my quiz, credits to [Web Dev Simplified](https://www.youtube.com/watch?v=riDzcEQbX6k)
-   To troubleshoot problems I had when defining media queries, I used [Stack Overflow](https://stackoverflow.com/questions/21441993/media-queries-doesnt-work)
-   Credits to my mentor Darío for encouraging me to continue to add things to improve my project.
-   Credits to this website for information regarding javascript [W3 Schools](https://www.w3schools.com/js/js_if_else.asp)
-   For design inspiration, I used [Scheme Color](https://www.schemecolor.com/matrix-code-green.php)
-   For early inspiration of the website I followed [Brian Design on Youtube](https://www.youtube.com/watch?v=f4fB9Xg2JEY)
-   For arrow functions, I used [W3 Schools](https://www.w3schools.com/js/js_arrow_function.asp)
-   For more design inspiration, I used [Coding Nepal](https://www.codingnepalweb.com/quiz-app-with-timer-javascript/)
     