pipeline {
    agent any

    environment {
        VENV = "v_env"
        QT_QPA_PLATFORM = "offscreen"
    }

    triggers {
        githubPush()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            steps {
                sh '''
                    python3 -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install -r requirements-dev.txt
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    flake8 src/ scripts/ tests/
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    python3 -m scripts.run_tests
                '''
            }
        }

        stage('Build') {
            when {
                branch 'main'
            }
            steps {
                sh '''
                    . ${VENV}/bin/activate
                    python3 -m scripts.build
                '''
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/*.xml'
        }
        failure {
            echo 'Pipeline failed'
        }
        success {
            echo 'Pipeline succeeded'
        }
    }
}
