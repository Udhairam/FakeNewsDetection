pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.8' // Modify if needed
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo 'Cloning the repository...'
                    checkout scm
                }
            }
        }

        stage('Set up Python') {
            steps {
                script {
                    echo 'Setting up Python environment...'
                    sh 'python3 --version'
                    sh 'pip install --upgrade pip'
                    sh 'pip install notebook pandas numpy' // Add other dependencies if needed
                }
            }
        }

        stage('Execute Notebook') {
            steps {
                script {
                    echo 'Converting and executing the notebook...'
                    sh 'jupyter nbconvert --to script *.ipynb' // Convert .ipynb to .py
                    sh 'python3 *.py' // Execute the converted Python script
                }
            }
        }

        stage('Archive Results') {
            steps {
                script {
                    echo 'Archiving output...'
                    archiveArtifacts artifacts: '**/*.ipynb, **/*.py', fingerprint: true
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs for errors.'
        }
    }
}
