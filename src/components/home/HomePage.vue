<script setup>
import { ref } from 'vue'
import HomeCard from '/src/components/home/HomeCard.vue'

const aboutMeData = ref({
  title: "Here's some thing about me.",
  data: [
    `I've <b>worked with data</b> in a bunch of different industries: <a href="https://en.wikipedia.org/wiki/Industrial_internet_of_things" target="_blank">IIoT</a>, Lending & Insurance, Application User Tracking, Marketing, Hotel & Airline, and Parking.`,
    `I <b>studied mathematics</b> in grad school. I worked in <a href="https://en.wikipedia.org/wiki/Algebraic_topology" target="_blank">algebraic topology</a>. Still love reading about topology being applied to data &mdash; one day I hope it becomes useful!`,
    `I've done <b>freelance <a href="https://en.wikipedia.org/wiki/Copy_editing" target="_blank">copy editing</a></b> since undergrad. <i>I hope you don't find any grammar issues on this page.</i>`
  ]
})

const appsListData = ref({
  title: "Here's some little apps I've made.",
  data: [
    `<a href="#/flags">Flag Guesser</a>: Guess the flag!`,
    `<a href="#/scene-starter">Improv Scene Starter Suggestion Generator</a>: Generates an emotion and some lines from chat-GPT.  Some lines are weird but it did its best.`,
    `<a href="#/facial-expressions">Facial Expressions</a>: Gives a random face emoji.  I used this when I had to practice different facial expressions for a Clowning class.`,
    `<a href="#/bass-practice">Bass Practice</a>: Gives a random practice routine for bass guitar.`,
    `<a href="#/vocal-practice">Vocal Practice</a>: Gives a random practice routine for vocal lessons.`,
    `<a href="#/dance-practice">Dance Practice</a>: Gives a random practice routine for misc dance lessons.`,
    `<a href="#/dice">Dice Roller</a>: Roll some dice.  I need to roll dice a lot.`
  ]
})

const codeAndTechData = ref({
  title: "Here's some code things I've done.",
  data: [
    `My <a href="https://github.com/jsal13/dotfiles" target="_blank">dotfiles</a> (<i>"What's a <a href="https://dotfiles.github.io/" target="_blank">dotfile?</a>"</i>)`,
    `<a href="https://github.com/jsal13/cookiecutter-pytemplate" target="_blank">My Python Cookiecutter template Template</a>`,
    `<a href="https://github.com/jsal13/toys" target="_blank">Toys for DE/ML/DS stuff</a>`
  ]
})
</script>

<template>
  <div class="home">
    <HomeCard :itemData="aboutMeData" />
    <HomeCard :itemData="appsListData" />
    <HomeCard :itemData="codeAndTechData" />
    <hr />
    <p>Have a good day! :']</p>
  </div>
</template>

<style>
.list-title {
  font-size: 1.2rem;
}
</style>
