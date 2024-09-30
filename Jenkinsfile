/* groovylint-disable-next-line CompileStatic */
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pull code from the Git repository
                git url: 'https://github.com/shkumar45/simple_test.git', branch: 'main'
            }
        }

        stage('Set Up Python') {
            steps {
                // Install Python dependencies
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run Python unit tests
                sh 'source venv/bin/activate && python -m unittest discover'
            }
        }
    }

    post {
        always {
            // Clean workspace after build
            cleanWs()
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
