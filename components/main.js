// Replaces the #persons div with the Vue app.

import Vue from 'vue';
import Persons from './persons.vue';

new Vue({
  el: '#persons',
  render: (createElement) => {
    return createElement('persons');
  },
  components: {
    persons: Persons
  }
})
