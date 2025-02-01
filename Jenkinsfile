pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://your-git-repo-url.git'  // Replace with your actual repo URL
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                script {
                    sh 'python3 -m venv venv'  // Create virtual environment
                    sh 'source venv/bin/activate'  // Activate virtual environment
                    sh 'pip install -r requirements.txt || echo "No requirements.txt found"'  // Install dependencies if available
                }
            }
        }
        
        stage('Run Python Script') {
            steps {
                sh 'source venv/bin/activate && python script.py'  // Run the script
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed! Check the logs.'
        }
    }
}
