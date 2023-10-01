<script setup>
import { onMounted, ref, watch } from 'vue'
import { countries } from '/src/data/countries'
import FlagsImage from '/src/components/apps/flags/FlagsImage.vue'

const countryData = ref({
  abbr: 'ac',
  name: 'Ascension Island',
  region: 'Territories and Minor Islands'
})
const countryAbbr = ref('az')
const countryName = ref('Ascension Island')
const showAnswer = ref(false)

onMounted(() => {
  GetRandomCountry()
})

watch(
  () => countryData.value,
  (value) => {
    countryAbbr.value = value['abbr']
    countryName.value = value['name']
  }
)

function NewRound() {
  showAnswer.value = false
  GetRandomCountry()
}

function GetRandomCountry() {
  countryData.value = countries[Math.floor(Math.random() * countries.length)]
}
</script>

<template>
  <div class="flags">
    <h1>Flag Guesser</h1>
    <hr />
    <FlagsImage class="m-4" :countryAbbr="countryAbbr" />
    <hr />
    <p class="h4 text-center" v-if="showAnswer">{{ countryName }}</p>
    <hr />
    <div class="d-inline-flex flex-column mb-4">
      <button type="button" class="btn text-light btn-info mb-2" @click="showAnswer = !showAnswer">
        Show Answer
      </button>
      <button type="button" class="btn btn-primary" @click="NewRound">
        <b>New Flag!</b>
      </button>
    </div>
  </div>
</template>
