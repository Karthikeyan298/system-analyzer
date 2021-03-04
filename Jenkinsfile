pipeline { 
    agent any 
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Test') { 
            agent {
                docker {
                    image 'python:3-alpine' 
                }
            }
            steps {
                sh "apk update"
                sh "apk add git"
                sh "git clone 'https://github.com/Karthikeyan298/system-analyzer.git' && cd system-analyzer"
                sh 'pip3 install pybuilder' 
                sh 'pyb run_unit_tests'
            }
        }
        // stage('Build'){
        //     steps {
        //         sh 'make check'
        //         junit 'reports/**/*.xml' 
        //     }
        // }
        // stage('Deploy') {
        //     steps {
        //         sh 'make publish'
        //     }
        }

    
}