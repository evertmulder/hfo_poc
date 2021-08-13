pipeline {
  agent {
    node {
      label 'none'
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
        sh 'ls -la'
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