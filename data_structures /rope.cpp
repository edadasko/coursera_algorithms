/*
Rope
Task. You are given a string S and you have to process n queries.
      Each query is described by three integers i, j, k and means to cut
      substring S[i..j] (i and j are 0-based) from the string and then insert
      it after the k-th symbol of the remaining string (if the symbols are
      numbered from 1). If k = 0, S[i..j] is inserted in the beginning.
Input Format. The first line contains the initial string S. The second line contains
               the number of queries q. Next q lines contain triples of integers i, j, k.
Output Format. Output the string after all 𝑞 queries.
*/

#include <iostream>
#include <stack>

struct Vertex {
    int size;
    char symbol;
    Vertex* left;
    Vertex* right;
    Vertex* parent;
    Vertex(){}
    Vertex(int size, char symbol, Vertex* left, Vertex* right, Vertex* parent)
    : size(size), symbol(symbol), left(left), right(right), parent(parent) {}
};

class Rope{
public:
    Rope(){
        root = NULL;
    }
    
    Rope(std::string s){
        length = (int)s.size();
        root = new Vertex(length, s[0], NULL, NULL, NULL);
        Vertex* v = root;
        for (int i = 1; i < length; i++){
            v->right = new Vertex(length - i, s[i], NULL, NULL, v);
            v = v->right;
        }
    }
    
    void moveSubstring(int l, int r, int pos) {
        Vertex* left = NULL;
        Vertex* substring = NULL;
        Vertex* right = NULL;
        _split(l, left, substring);
        _split(substring, r - l + 1, substring, right);
        Vertex* s_without_substr = _merge(left, right);
        _split(s_without_substr, pos, left, right);
        root = _merge(_merge(left, substring), right);
    }
    
    void printString(){
        std::stack<Vertex*> nodes;
        Vertex* curr = root;
        while (curr || !nodes.empty()){
            while (curr){
                nodes.push(curr);
                curr = curr->left;
            }
            curr = nodes.top();
            nodes.pop();
            std::cout << curr->symbol;
            curr = curr->right;
        }
    }
    
private:
    Vertex* root;
    int length;
    
    void _update(Vertex* v){
        if (v == NULL) return;
        v->size = 1 + (v->left != NULL ? v->left->size : 0)
                    + (v->right != NULL ? v->right->size : 0);
        if (v == NULL) return;
        if (v->left != NULL)
            v->left->parent = v;
        if (v->right != NULL)
            v->right->parent = v;
    }
    
    void _small_rotation(Vertex* v) {
        Vertex* parent = v->parent;
        if (parent == NULL)
            return;
        Vertex* grandparent = v->parent->parent;
        if (parent->left == v) {
            Vertex* m = v->right;
            v->right = parent;
            parent->left = m;
        } else {
            Vertex* m = v->left;
            v->left = parent;
            parent->right = m;
        }
        _update(parent);
        _update(v);
        v->parent = grandparent;
        if (grandparent != NULL) {
            if (grandparent->left == parent)
                grandparent->left = v;
            else
                grandparent->right = v;
        }
    }
    
    void _big_rotation(Vertex* v) {
        if ((v->parent->left == v && v->parent->parent->left == v->parent) ||
            (v->parent->right == v && v->parent->parent->right == v->parent)) {
            // Zig-zig
            _small_rotation(v->parent);
            _small_rotation(v);
        } else {
            // Zig-zag
            _small_rotation(v);
            _small_rotation(v);
        }
    }
    
    void _splay(Vertex* v) {
        _splay(root, v);
    };
    
    void _splay(Vertex*& node, Vertex* v) {
        if (v == NULL) return;
        while (v->parent != NULL) {
            if (v->parent->parent == NULL) {
                // Zig
                _small_rotation(v);
                break;
            }
            _big_rotation(v);
        }
        node = v;
    };
    
    Vertex* _find(int key){
        return _find(root, key);
    }
    
    Vertex* _find(Vertex*& node, int size) {
        Vertex* v = node;
        while (v) {
            int s = (v->left ? v->left->size : 0);
            if (size == s){
                break;
            } else if (size < s){
                v = v -> left;
            } else {
                v = v -> right;
                size -= s + 1;
            }
        }
        if (!v) return NULL;
        _splay(node, v);
        return node;
    }
    
    void _split(int key, Vertex*& left, Vertex*& right) {
        _split(root, key, left, right);
    }
    
    void _split(Vertex* node, int size, Vertex*& left, Vertex*& right) {
        Vertex* v = _find(node, size);
        if (!v) {
            left = node;
            right = NULL;
            return;
        };
        right = v;
        left = v -> left;
        if (left) left -> parent = NULL;
        right -> left = NULL;
        _update(left);
        _update(right);
    }
    
    Vertex* _merge(Vertex* left, Vertex* right) {
        if (left == NULL) return right;
        if (right == NULL) return left;
        Vertex* min_right = right;
        while (min_right->left != NULL)
            min_right = min_right->left;
        _splay(right, min_right);
        right->left = left;
        _update(right);
        return right;
    };
};

int main(){
    std::string s;
    std::cin >> s;
    Rope rope(s);
    int n;
    std::cin >> n;
    for (int i = 0; i < n; i++){
        int l, r, pos;
        std::cin >> l >> r >> pos;
        rope.moveSubstring(l, r, pos);
    }
    rope.printString();
    return 0;
}
