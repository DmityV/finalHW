<template>
    <div class="modal">
      <div class="modal-content">
        <slot></slot>
        <div class="buttons">
          <button class="button-send" @click="addPosts()">Отправить</button>
          <button class="button-cancel" @click="$emit('close')">Отменить</button>
        </div>
      </div>
    </div>
  </template>

 <script>
  export default {
    props: {
      addPosts: { type: Function }
    }
  }
</script>

  <style scoped>
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .modal-content {
    text-align: left;
    width: 700px;
    background-color: white;
    padding: 20px;
    border-radius: 4px;
  }
  .buttons {
    text-align: right;
  }
  .button-send {
    margin-right: 10px;
    background-color: rgb(39, 130, 59);
    color: white;
  }
  .button-cancel {
    border: 1px solid rgb(221, 221, 221);
    background-color: white;
    margin-right: 10px;
  }
  </style>