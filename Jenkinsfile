pipeline {
    agent any
    stages {
        stage('Checkout SCM') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], userRemoteConfigs: [[url: 'https://github.com/BibekSsahoo/Streamlit.git']]])
            }
        }
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/BibekSsahoo/Streamlit.git', branch: 'main'
            }
        }
        stage('Cleanup Stage') {
            steps {
                script {
                    def containers = sh(script: "docker ps -aq", returnStdout: true).trim()
                    if (containers) {
                        sh "docker rm -f ${containers}"
                    } else {
                        echo "No containers to remove"
                    }
                }
            }
        }
        stage('Build Docker Image') {
            when {
                expression {
                    return currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                // Your steps for building the Docker image
            }
        }
        stage('Run Docker Container') {
            when {
                expression {
                    return currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                // Your steps for running the Docker container
            }
        }
    }
}
