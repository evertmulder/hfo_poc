pipeline {
  agent {
    docker {
      image 'node:lts-alpine3.14'
    }

  }
  stages {
    stage('build') {
      steps {
        echo 'hello'
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