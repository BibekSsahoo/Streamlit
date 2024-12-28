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
        stage("Build Docker image") {
            steps {
                sh 'docker build -t myimage .'
            }
        }
        stage("Create Container") {
            steps {
                sh 'docker run -d -p 8501:8501 myimage'
            }
        }
    }
}
