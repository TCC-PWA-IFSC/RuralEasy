<script>
import axios from "axios";

//LOGIN - PARA IMPLEMENTAÇÕES FUTURAS

export default {
    data() {
        return {
            username: "",  
            password: ""   
        };
    },
    methods: {
        async login() {
            try {
                const response = await axios.post("127.0.0.1/auth/token/login/", {
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
