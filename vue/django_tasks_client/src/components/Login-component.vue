<!-- Não há mudanças no template -->
...

<script>
import axios from "axios";

export default {
    data() {
        return {
            username: "",  // Este corresponde ao campo "Usuário" do Produtor
            password: ""   // Este corresponde ao campo "Senha" do Produtor
        };
    },
    methods: {
        async login() {
            try {
                const response = await axios.post("YOUR_DJANGO_BACKEND_URL/auth/token/login/", {
                    username: this.username,
                    password: this.password
                });
                localStorage.setItem("access_token", response.data.access_token);
                this.$router.push("/protected-route");
            } catch (error) {
                console.error("Error during authentication:", error);
            }
        }
    }
};
</script>
