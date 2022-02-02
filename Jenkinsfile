pipeline {
    agent { label any }
    stages {
        stage('Build') { 
            steps {
                sh 'docker rm -f flask-api'
                sh 'docker rmi -f flask-app'
                sh 'docker build -t flask-app /app'
                sh 'docker run -d --network jenkins_bridge -h my-flask-app --name flask-api flask-app'
            }
        }
        stage('Run') { 
            steps {
                sh 'sleep 5'
                sh 'curl 172.18.0.4:80'
            }
        }
        stage('Test') { 
            steps {
                sh 'python /app/tests/e2e.py' 
            }
        }
    }
}
