class Solution:

	def inorder_list(self,p):
		res = []
		if p:
			inorder_list(self,q.left)
			res.append(q.data)
			inorder_list(self,q.right)
		return res		




    def isSameTree(self, p, q):
    
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        tree1_res = self.inorder_list(p)
        tree2_res = self.inorder_list(q)

        return tree1_res==tree2_res


