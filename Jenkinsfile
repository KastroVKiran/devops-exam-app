// Jenkinsfile

pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'flask-devops-app'
        DOCKER_REGISTRY = 'docker.io/kastrov'  // Your Docker Hub username
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/kastrov/devops-cert-exam.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('', 'dockerhub-credentials') {
                        docker.image(DOCKER_IMAGE).push('latest')
                    }
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                script {
                    sh '''
                    ssh -i /path/to/your/EC2-key.pem ec2-user@your-ec2-ip 'docker pull docker.io/kastrov/${DOCKER_IMAGE}:latest && docker-compose -f /path/to/your/docker-compose.yml up -d'
                    '''
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
