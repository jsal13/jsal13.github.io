<script setup>
import { onMounted, ref, watch } from 'vue'
import { countries } from '/src/data/countries'
import FlagsImage from '/src/components/apps/flags/FlagsImage.vue'
import SpoilerText from '/src/components/common/SpoilerText.vue';

const countryData = ref({ 'abbr': 'ac', 'name': "Ascension Island", 'region': 'Territories and Minor Islands' })
const countryAbbr = ref("az");
const countryName = ref("Ascension Island")


onMounted(() => {
  getRandomCountry()
});

watch(() => countryData.value, (value) => {
  countryAbbr.value = value["abbr"];
  countryName.value = value["name"]
})

function getRandomCountry() {
  countryData.value = countries[Math.floor(Math.random() * countries.length)];
}

</script>

<template>
  <div class="flags">
    <FlagsImage :countryAbbr="countryAbbr" />
    <br />
    <hr />
    <SpoilerText :text="countryName" size="24px" />
    <button type="button" class="btn btn-primary" @click="getRandomCountry()">Next Flag!</button>
  </div>
</template>
