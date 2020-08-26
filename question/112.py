def hasPathSum(self, root, sum):

    self.res = False

    def find(root, sum):

        if not root:
            return

        if root.val == sum:
            if not root.left and not root.right:
                self.res = True

            # Should NOT return here since it may not traverse
            # to the end of the branch yet
            # return

        find(root.left, sum - root.val)
        find(root.right, sum - root.val)

    find(root, sum)

    return self.res
