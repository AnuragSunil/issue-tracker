pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning repository...'
                // For GitHub pipeline jobs (not needed for local freestyle builds)
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t issue-tracker-app .'
            }
        }

        stage('Stop & Remove Old Container') {
            steps {
                echo 'Stopping any existing container...'
                sh '''
                docker stop issue-tracker-app || true
                docker rm issue-tracker-app || true
                '''
            }
        }

        stage('Run New Container') {
            steps {
                echo 'Running new container...'
                sh 'docker run -d -p 5000:5000 --name issue-tracker-app issue-tracker-app'
            }
        }
    }
}
