<script setup>
// Make this timer better.  Maybe give it a pause function.

import { ref, onMounted, watch } from 'vue';
import { countdown } from '/src/scripts/countdown'

const props = defineProps({ seconds: Number })

const endTime = ref(0)
const delta = ref(0)

const minsRemaining = ref(0)
const secsRemaining = ref()
const interval = ref(0)
const playing = ref(true)
const iconVal = ref('bi-pause')
const bgColor = ref("bg-success")

watch(() => delta.value, (val) => {
    minsRemaining.value = val.minutes;
    secsRemaining.value = val.seconds;
})

watch(() => playing.value, (val) => {
    if (val) {
        iconVal.value = 'bi-pause'
        bgColor.value = 'bg-success'
    }
    else {
        iconVal.value = 'bi-play-fill'
        bgColor.value = 'bg-info'
    }
})

function StartTimer(secondsRemaining) {
    endTime.value = new Date(new Date().getTime() + (secondsRemaining * 1000));
    delta.value = countdown(new Date(), endTime.value);
    playing.value = true
    interval.value = setInterval(UpdateTimer, 1000);
}

function UpdateTimer() {
    var now = new Date()
    delta.value = countdown(new Date(), endTime.value)
}

function ResetTimer() {
    clearInterval(interval.value)
    StartTimer(props.seconds);
}

function ToggleTimer() {
    if (playing.value) {
        PauseTimer()
    }
    else {
        StartTimer(minsRemaining.value * 60 + secsRemaining.value)
    }
}

function PauseTimer() {
    playing.value = false
    clearInterval(interval.value)
}

onMounted(() => {
    ResetTimer();
})

</script>

<template>
    <div class="timer d-flex mb-2">
        <table :class="bgColor + ' timer-table'">
            <tr>
                <td><button class="btn btn-sm rounded-2'" @click="ToggleTimer"> <i
                            :class="iconVal + ' play-icon text-light'"></i></button></td>
                <td><button class="btn btn-sm rounded-2'" @click="ResetTimer"><i
                            class="bi-arrow-counterclockwise play-icon text-light"></i></button>
                </td>
                <td>
                    <span class="time-left text-light pe-3">{{ minsRemaining }}m {{ secsRemaining
                    }}s</span>
                </td>
            </tr>
        </table>


    </div>
</template>

<style>
.time-left {
    font-size: 1.25rem;
    font-weight: bold;
    text-shadow: 1px 1px #0f0f0f;
}

.timer-table {
    border: 1px solid darkgray;
    border-radius: 0.25rem;
    border-collapse: separate;
}

.timer-table td {
    padding-left: 0.25rem;
    padding-right: 0.25rem;
}
</style>