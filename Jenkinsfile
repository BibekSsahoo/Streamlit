pipeline {
    agent any
    stages {
        stage("checkout Code") {
            steps {
                git url:'https://github.com/BibekSsahoo/Streamlit.git', branch:'main'
            }
        }
        stage("Cleanup Stage") {
            steps {
                sh 'docker rm -f $(docker ps -aq)'
            }
        }

        stage("Build Dokcer Image") {
            steps {
                sh 'docker build -t streamlit-app .'
            } 
        }
        stage("Run Docker Container") {
            steps {
                sh 'docker run -d -p 8501:8501 streamlit-app'
            }
        }
    }
}
