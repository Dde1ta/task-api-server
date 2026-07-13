pipeline{
    agent any

    tools {
        dockerTool 'docker-cli'
    }

    environment {
        DOCKER_TOKEN = credentials("1")
        PATH = "${WORKSPACE}/docker:${env.PATH}"
    }

    stages{
        stage('Install Docker CLI Manually') {
            steps {
                sh '''
                if ! command -v docker &> /dev/null; then
                    echo "Downloading modern Docker CLI..."
                    curl -fsSL https://download.docker.com/linux/static/stable/x86_64/docker-24.0.9.tgz -o docker.tgz
                    tar -xzf docker.tgz
                    chmod +x docker/docker
                else
                    echo "Docker CLI already installed!"
                fi
                '''
            }
        }

        stage("environment setup"){
            steps{
                withCredentials([usernamePassword(credentialsId: '1',
                                                  passwordVariable: 'DOCKER_PASS',
                                                  usernameVariable: 'DOCKER_USER')]) {
                    sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
                }
            }
        }

        stage("pull"){
            steps{
                git branch: 'main', url: 'https://github.com/Dde1ta/task-api-server.git'
                sh 'ls'
                sh 'pwd'
            }
        }

        stage("build"){
            steps{
                script {
                    docker.build("dde1ta/simple-fast-api-app:latest")
                }
            }
        }

        stage("test"){
            steps{
                sh 'docker run --name test_container --rm -d dde1ta/simple-fast-api-app:latest'
                sh 'docker exec test_container pytest'
                sh 'docker stop test_container'
            }
        }

        stage("push"){
            steps{
                sh 'docker push dde1ta/simple-fast-api-app:latest'
            }
        }
    }
}