pipeline{
    agen any
    stages{
        stage{
            steps{
                sh 'docker rm -f $(docker ps -aq)
            }
        }
        stage{
            steps{
                sh 'docker run -d -p 8051:8051 myimage'
            }
        }
    }

}
