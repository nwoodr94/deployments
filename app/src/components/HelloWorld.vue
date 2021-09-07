<template>
  <v-container fill-height>
    <v-row align="center" justify="center">
      <v-col>
        <v-card>
          <v-card-text
            ><v-form :submit="submit">
              <v-file-input v-model="fileOne">File One</v-file-input>
              <v-file-input v-model="fileTwo">File Two</v-file-input>
            </v-form>
            <v-btn v-on:click="submit">Submit</v-btn></v-card-text
          >
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
  data: () => ({
    fileOne: null,
    fileTwo: null,
  }),
  methods: {
    async submit() {
      let form = new FormData();
      form.append("files", this.fileOne);
      form.append("files", this.fileTwo);
      await axios
        .post("http://localhost:5000/upload", form, {
          headers: {
            "Content-Type": `multipart/form-data; boundary=${form._boundary}`,
          },
        })
        .then((response) => {
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
