<template>
  <v-app>
    <v-app-bar app color="primary" dark>Deployments</v-app-bar>

    <v-main>
      <HelloWorld :msg="msg" />
    </v-main>
  </v-app>
</template>

<script>
import HelloWorld from "./components/HelloWorld";
import axios from "axios";

export default {
  name: "App",

  components: {
    HelloWorld,
  },

  data: () => ({
    msg: null,
  }),
  mounted: async function () {
    this.msg = await axios
      .get("http://localhost:5000/hello")
      .then((response) => {
        return response.data;
      });
  },
};
</script>
