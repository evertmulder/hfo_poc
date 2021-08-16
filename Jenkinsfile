pipeline {
  agent any
  stages {
    stage('build') {
      parallel {
        stage('build') {
          steps {
            echo 'hello'
          }
        }

        stage('Sleep') {
          steps {
            sleep 3
          }
        }

      }
    }

    stage('test') {
      steps {
        sh '''ls -la

'''
        sh 'pwd'
      }
    }

    stage('deploy') {
      steps {
        sleep 2
        echo 'deploy'
      }
    }

  }
}