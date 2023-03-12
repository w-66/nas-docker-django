#!/bin/bash

# 配置远程仓库地址
GITEE_REMOTE="giteeDjango"
GITHUB_REMOTE="githubDjango"

# 获取当前分支名
BRANCH=$(git symbolic-ref --short HEAD)

# 上传到 Gitee
echo "Pushing to Gitee..."
git push $GITEE_REMOTE $BRANCH

# 上传到 Github
echo "Pushing to Github..."
git push $GITHUB_REMOTE $BRANCH

# 结束提示
echo "Push completed."
