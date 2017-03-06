<template>
  <div id="persons">
    
    <!-- Header -->
    <div class="header-bg">
      <div class="header">
        <h1>SKoPM</h1>
        <h2>Some Kind of Persons Manager</h2>
      </div>
    </div>
    
    <!-- persons table -->
    <div class="table">
      <div v-for=" person in persons " class="table-item">
        <!-- Text version of person data -->
        <div v-if="edit_item === null || edit_item.id !== person.id" class="pure-g">
          <span class="pure-u-1 pure-u-xl-3-8"><strong>Name:</strong> {{ person.first_name }} {{ person.last_name }}</span>
          <span class="pure-u-1 pure-u-xl-1-6"><strong>Date of Birth:</strong> {{ person.date_of_birth }}</span>
          <span class="pure-u-1 pure-u-xl-1-6"><strong>Zip Code:</strong> {{ person.zip_code }}</span>
          <span class="pure-u-1 pure-u-xl-7-24 button-wrapper">
            <button @click="set_edit_item( person )" class="pure-button edit">Edit</button>
            <button @click="delete_item = person" class="pure-button delete">Delete</button>
          </span>
        </div>
        <form v-else class="pure-g">
          <!-- Input version of update data -->
          <span class="pure-u-1 pure-u-xl-3-8"><strong>Name:</strong><br class="edit-break"> <input v-model="edit_item.first_name" placeholder="First"> <input v-model="edit_item.last_name" placeholder="Last"></span>
          <span class="pure-u-1 pure-u-xl-1-6"><strong>Date of Birth:</strong><br class="edit-break"> <input v-model="edit_item.date_of_birth" placeholder="MM/DD/YYYY"></span>
          <span class="pure-u-1 pure-u-xl-1-6"><strong>Zip Code:</strong><br class="edit-break"> <input v-model="edit_item.zip_code" placeholder="12345"></span>
          <span class="pure-u-1 pure-u-xl-7-24 button-wrapper">
            <button @click.prevent="submit_edit()" class="pure-button edit">Update</button>
            <button @click.prevent="cancel_edit()" class="pure-button">Cancel</button>
          </span>
        </form>
      </div>
      
      <!-- new item section -->
      <div class="new">
        <div v-if="new_item === null">
          <button class="pure-button edit" @click.prevent="create_new()">+ New</button>
        </div>
        <form v-else class="pure-g">
          <span class="pure-u-1 pure-u-xl-3-8"><strong>Name:</strong><br class="edit-break"> <input v-model="new_item.first_name" placeholder="First"> <input v-model="new_item.last_name" placeholder="Last"></span>
          <span class="pure-u-1 pure-u-xl-1-6"><strong>Date of Birth:</strong><br class="edit-break"> <input v-model="new_item.date_of_birth" placeholder="MM/DD/YYYY"></span>
          <span class="pure-u-1 pure-u-xl-1-6"><strong>Zip Code:</strong><br class="edit-break"> <input v-model="new_item.zip_code" placeholder="12345"></span>
          <span class="pure-u-1 pure-u-xl-7-24 button-wrapper">
            <button @click.prevent="submit_new()" class="pure-button edit">Create</button>
            <button @click.prevent="cancel_new()" class="pure-button">Cancel</button>
          </span>
        </form>
      </div>
    </div>
    
    <!-- confirm delete modal -->
    <transition name="modal">
      <div v-if="delete_item !== null" class="delete-modal">
        <div class="delete-modal-body">
          <h1>Delete <strong>{{delete_item.first_name}} {{delete_item.last_name}}</strong>?</h1>
          <div>
            <button class="pure-button delete" @click="submit_delete()">Yes</button>
            <button class="pure-button" @click="delete_item = null">No</button>
          </div>
        </div>
      </div>
    </transition>

  </div>
</template>

<style scoped>
  /* TODO: switch to less and clean up this mess */
  /* TODO: responsive design for mid-sized devices — too much whitespace*/
  
  #persons {
    margin: 30px;
    display: flex;
    flex-direction: column;
  }
  
  .header-bg {
    width: 100vw;
    background-color: rgb(200,203,200);
    height: 87px;
    margin: -30px -30px 0;
    box-shadow: 1px 2px 3px rgba(0,0,0,0.1) inset;
  }
  .header {
    color: white;
    background-color: #0d2b0d;
    width: 350px;
    padding: 10px 20px;
    box-shadow: 4px 5px 4px rgba(0,0,0,0.11);
    font-family: 'Proza Libre', 'Lato', sans-serif;
    height: 70px;
  }
  @media screen and (orientation: portrait) {
    .header {
      width: 100vw;
    }
  }
  
  h1 {
    margin: auto;
  }
  h2 {
    margin: auto;
    font-weight: 600;
    font-size: 1.1em;
    font-variant: small-caps;
  }
 
  .table {
    margin: 10px auto;
  }
  @media screen and (min-width: 1280px) {
    .table {
      width: 1280px;
    }
  }
  
  .table-item {
    padding: 5px 10px;
    border-bottom: 1px solid rgba(0,0,0,0.1);
  }
  .table-item, .table-item > * {
    width: 100%;
    min-height: 42px;
  }
  input {
    border: 1px solid #ddd;
    border-radius: 3px;
    padding: 1px 5px;
    box-shadow: 2px 1px 3px rgba(0,0,0,0.1) inset;
  }
  @media screen and (max-width: 1279px) {
    .table-item {
      padding: 20px 10px 15px;
      border-bottom: 1px solid rgba(0,0,0,0.5);
    }
    .edit-break {
      display: none;
    }
    input {
      margin-left: 10px;
    }
  }
  @media screen and (max-width: 1279px) and (orientation: portait) {
    .pure-u-1 {
      line-height: 75px;
    }
  }
  @media screen and (max-width: 1279px) and (orientation: landscape) {
    .pure-u-1 {
      line-height: 35px;
    }
  }
  
  button.edit {
    margin-left: auto;
  }
  button:not(.edit) {
    margin-right: 40px;
  }
  
  input {
    max-width: 100%;
  }
  
  button.edit {
    color: white;
    background-color: #007300;
  }
  button.delete {
    color: white;
    background-color: #d20000;
  }
  
  .button-wrapper {
    height: 100%;
    display: flex;
  }
  button {
    margin: auto 10px auto;
  }
  .pure-u-1 {
    margin: auto 0;
  }
  @media screen and (max-width: 1279px) {
    .button-wrapper {
      margin-top: 20px;
    }
  }
  
  .new {
    padding-top: 10px;
  }
  .new > div {
    display: flex;
    height: 42px;
  }
  .new > div button {
    margin: auto;
  }
  .new > form {
    width: 100%;
    padding: 10px;
  }
  
  .delete-modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(0,0,0,0.2);
    display: flex;
  }
  .delete-modal-body {
    background-color: white;
    margin: auto;
    padding: 10px 0 0;
    min-width: 250px;
  }
  .delete-modal h1{
    font-size: 1.2em;
    font-weight: 400;
    padding-bottom: 10px;
    padding: 0 10px 10px;
  }
  .delete-modal-body div {
    background-color: rgb(175,175,175);
    padding: 10px;
    display: flex;
    box-shadow: 2px 1px 1px rgba(0,0,0,0.3);
  }
  .delete-modal-body button {
    margin: auto;
  }
  
  .modal-enter, .modal-leave-to {
    background-color: rgba(0,0,0,0);
  }
  .modal-enter-active, .modal-leave-active {
    transition: background-color 0.2s cubic-bezier(0.77, 0, 0.175, 1);
  }
  
  .modal-enter .delete-modal-body, .modal-leave-to .delete-modal-body {
    transform: scale(0.2);
  }
  .modal-enter-active .delete-modal-body, .modal-leave-active .delete-modal-body {
    transition: transform 0.2s cubic-bezier(0.895, 0.03, 0.685, 0.22);
  }
</style>

<script>
  export default {
    data() {
      return {
        persons: [], // data for persons table
        edit_item: null, // stores data for update when active
        new_item: null, // stores data when new is active
        delete_item: null // stores data for delete confirmation
      };
    },
    created() {
      // fetch the table data
      var xhr = new XMLHttpRequest();
      xhr.open("GET", "persons", true);
      
      xhr.onload = () => {
        if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
          this.persons = JSON.parse( xhr.responseText );
          this.persons.sort( (a,b) => {
            if ( a.id < b.id ) {
              return -1;
            }
            else if ( a.id > b.id ) {
              return 1;
            }
            else {
              return 0;
            }
          });
        }
      };
      
      xhr.send();
    },
    methods: {
      set_edit_item( item ) { // set an item for edit mode. works on copy
        this.edit_item = Object.assign( {}, item );
      },
      submit_edit() { // sumbit edit_item to server: updates database
        var xhr = new XMLHttpRequest();
        xhr.open("PUT", "persons", true);
        xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
        
        xhr.onload = () => {
          if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
            let data = JSON.parse( xhr.responseText );
            
            // update the correct row
            for ( let person of this.persons ) {
              if ( person.id === data.id ) {
                for ( let key in data ) {
                  person[key] = data[key];
                }
                break;
              }
            }
            this.edit_item = null; // leave edit mode
          }
        };
        
        xhr.send( JSON.stringify( this.edit_item ) );
      },
      cancel_edit() { // cancel editing the item
        this.edit_item = null;
      },
      create_new() { // create new_item
        this.new_item = {first_name: '', last_name: '', date_of_birth: '', zip_code: ''};
      },
      submit_new() { // sumbit new_item to server: adds to database
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "persons", true);
        xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
        
        xhr.onload = () => {
          if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
            let data = JSON.parse( xhr.responseText );
            this.persons.push(data); // add item to the table
            
            this.new_item = null;
          }
        };
        
        xhr.send( JSON.stringify( this.new_item ) );
      },
      cancel_new() { // cancel creating new item
        this.new_item = null;
      },
      submit_delete() { // deletes delete_item from the database
        var xhr = new XMLHttpRequest();
        xhr.open("DELETE", "persons", true);
        xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
        
        xhr.onload = () => {
          if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
            let data = JSON.parse( xhr.responseText );
            for ( let i=0; i<this.persons.length; i++ ) {
              console.log(i)
              if ( this.persons[i].id === data.id ) {
                this.$delete(this.persons, i); // remove from table
                this.delete_item = null;
                break;
              }
            }
          }
        };
        
        xhr.send( JSON.stringify( { id: this.delete_item.id } ) );
      }
    }
  };
</script>
