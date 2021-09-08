<template>
  <v-app>
    <v-app-bar app color="primary" dark>Deployments</v-app-bar>

    <v-main>
      {{ msg }}
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import axios from "axios";

export default {
  name: "App",
  data: () => ({
    msg: null,
  }),
  mounted: async function () {
    this.msg = await axios
      .get("http://localhost:5000/hello")
      .then((response) => {
        return response.data;
      })
      .catch((error) => {
        return error;
      });
  },
};
</script>
