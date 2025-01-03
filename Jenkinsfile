pipeline {
    agent {
        node {
            label 'Jenkins_slave'
        }
    }
    
    stages {
        stage('Checkout code') {
            steps {
                git url: 'https://github.com/BibekSsahoo/Streamlit.git', branch: 'main'
            }
        }
       stage('cleanup stage') {
            steps {
                sh 'docker rmi -f myapp'
                sh 'docker rm -f $(docker ps -aq)'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myapp .'
            }
        }
       stage('Build and Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub_Cred', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    sh 'docker tag myrepo $DOCKER_USERNAME/myapp'
                    sh 'docker push $DOCKER_USERNAME/myapp'
                }
                   
            }
        }
        stage('Deploy application to kubernetes') {
            steps {
                sh 'kubectl apply -f my-deployment.yml'
            }
        }
    }
}
