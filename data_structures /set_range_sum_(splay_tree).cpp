/*
 Set with range sums (Splay Tree solution)
 Task. Implement a data structure that stores a set S of integers with
       the following allowed operations:
        - add(i) — add integer i into the set S (if it was there already, the set doesn’t change).
        - del(i) — remove integer i from the set S (if there was no such element, nothing happens).
        - find(i) — check whether i is in the set S or not.
        - sum(l,r)—output the sum of all elements v in 𝑆 such that l<=v<=r.
 Input Format. Initially the set S is empty. The first line contains n — the number of operations.
               The next n lines contain operations. Each operation is one of the following:
               - “+ i" — which means add some integer to 𝑆,
               - “- i" — which means del some integer from 𝑆,
               - “? i" — which means find some integer in 𝑆,
               - “s l r" — which means compute the sum of all elements of S within some range of values.
               However, to make sure that your solution can work in an online fashion, each request will
               actually depend on the result of the last sum request. Denote 𝑀 = 1 000 000 001.
               At any moment, let x be the result of the last sum operation, or just 0 if there were
               no sum operations before. Then
               - “+ i" means add((i + x) mod M),
               - “- i" means del((i + x) mod M),
               - “? i" means find((i + x) mod M),
               - “s l r" means sum((l + x) mod M, (r + x) mod M).
 Output Format. For each find request, just output “Found" or “Not found"
                (without quotes; note that the first letter is capital) depending
                on whether (i + x) mod M is in S or not. For each sum query, output
                the sum of all the values 𝑣 in 𝑆 such that ((l + x) mod 𝑀) <= v <= ((r + x) mod M).
 */

#include <iostream>

struct Vertex {
    int key;
    long long sum;
    Vertex* left;
    Vertex* right;
    Vertex* parent;
    Vertex(){}
    Vertex(int key, long long sum, Vertex* left, Vertex* right, Vertex* parent)
    : key(key), sum(sum), left(left), right(right), parent(parent) {}
};

class SplayTree {
public:
    SplayTree(){
        root = NULL;
    }
    
    void insert(int key) {
        Vertex* left = NULL;
        Vertex* right = NULL;
        Vertex* new_vertex = NULL;
        _split(key, left, right);
        if (!right || right -> key != key)
            new_vertex = new Vertex(key, key, NULL, NULL, NULL);
        root = _merge(_merge(left, new_vertex), right);
    }
    
    void erase(int key) {
        Vertex* f = _find(key);
        if (!f || f -> key != key)
            return;
        root = _merge(f -> left, f -> right);
        if (root) {
            Vertex* p = root -> parent;
            root -> parent = NULL;
            delete p;
        }
    }
    
    bool find(int key) {
        Vertex* f = _find(key);
        if (!f || f -> key != key)
            return false;
        return true;
    }
    
    long long sum(int from, int to) {
        Vertex* left = NULL;
        Vertex* middle = NULL;
        Vertex* right = NULL;
        _split(from, left, middle);
        _split(middle, to + 1, middle, right);
        long long ans = 0;
        if (middle) ans = middle -> sum;
        root = _merge(left, _merge(middle, right));
        return ans;
    }
    
private:
    Vertex* root;
    
    void _update(Vertex* v) {
        if (v == NULL) return;
        v->sum = v->key + (v->left != NULL ? v->left->sum : 0ll)
                        + (v->right != NULL ? v->right->sum : 0ll);
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
    
    Vertex* _find(Vertex*& node, int key) {
        Vertex* v = node;
        while (v) {
            if (key == v->key) {
                break;
            } else if (key > v->key) {
                if (v -> right){
                    v = v -> right;
                } else break;
            } else {
                if (v -> left){
                    v = v -> left;
                } else break;
            }
        }
        _splay(node, v);
        return node;
    }
    
    void _split(int key, Vertex*& left, Vertex*& right) {
        _split(root, key, left, right);
    }
    
    void _split(Vertex* node, int key, Vertex*& left, Vertex*& right) {
        Vertex* v = _find(node, key);
        if (!v) return;
        if (v->key >= key) {
            right = v;
            left = v -> left;
            if (left) left -> parent = NULL;
            right -> left = NULL;
        }
        else {
            left = v;
            right = v -> right;
            if (right) right -> parent = NULL;
            left -> right = NULL;
        }
        _update(left);
        _update(right);
    };
    
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


const int MOD = 1000000001;

int main(){
    SplayTree t;
    int n;
    std::cin >> n;
    int last_sum_result = 0;
    for (int i = 0; i < n; i++) {
        std::string buffer;
        std::cin >> buffer;
        char type = buffer[0];
        switch (type) {
            case '+' : {
                int x;
                std::cin >> x;
                t.insert((x + last_sum_result) % MOD);
            } break;
            case '-' : {
                int x;
                std::cin >> x;
                t.erase((x + last_sum_result) % MOD);
            } break;
            case '?' : {
                int x;
                std::cin >> x;
                std::cout << (t.find((x + last_sum_result) % MOD)
                              ? "Found\n" : "Not found\n");
            } break;
            case 's' : {
                int l, r;
                std::cin >> l >> r;
                long long res = t.sum((l + last_sum_result) % MOD,
                                      (r + last_sum_result) % MOD);
                std::cout << res << std::endl;
                last_sum_result = int(res % MOD);
            }
        }
    }
    return 0;
}
