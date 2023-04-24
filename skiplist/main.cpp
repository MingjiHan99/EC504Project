
#include <iostream>
#include <memory>
#include <random>
#include <optional>
using namespace std;

template<typename K, typename V>
struct Node {
    K key;
    V value;
    vector<shared_ptr<Node> > next_ptrs;
    int level;
    Node(const K& key, const V& value, const int& level) : key(key), value(value), level(level) {
        for (int i = 0; i < level; ++i) {
            next_ptrs.push_back(nullptr);
        }
    }
};

template<typename K, typename V>
class SkipList {
public:
    SkipList(const double& p, const int& max_level) : p(p), max_level(max_level),distribution(0.0, 1.0) {
        head = make_shared<Node<K, V> >(K(), V(), max_level);
    }

    void set(const K& key, const V& value) {
        // If key has existed, update the value.
        auto ptr = find_ptr(key);
        if (ptr != nullptr) {
            ptr->value = value;
            return;
        }
        // If key has not existed, insert a new node.
        int level = random_level();
        shared_ptr<Node<K, V> > node = make_shared<Node<K, V> >(key, value, level);
        
        vector<shared_ptr<Node<K, V> > > prev_ptrs(max_level, nullptr);
        auto p = head;
        for (int i = level - 1; i >= 0; --i) {
            while (p->next_ptrs[i] != nullptr && p->next_ptrs[i]->key < key) {
                p = p->next_ptrs[i];
            }
            prev_ptrs[i] = p;
        }

        for (int i = 0; i < level; ++i) {
            node->next_ptrs[i] = prev_ptrs[i]->next_ptrs[i];
            prev_ptrs[i]->next_ptrs[i] = node;
        }
    }
    
    void remove(const K& key) {
        // If key has not existed, ignore remove operation.
        auto ptr = find_ptr(key);
        if (ptr == nullptr) {
            return;
        }
        // If key has existed, remove the node.
        auto p = head;
        vector<shared_ptr<Node<K, V> > > prev_ptrs(max_level, nullptr);
        for (int i = max_level - 1; i >= 0; --i) {
            while (p->next_ptrs[i] != nullptr && p->next_ptrs[i]->key < key) {
                p = p->next_ptrs[i];
            }
            prev_ptrs[i] = p;
        }
        for (int i = 0; i < max_level; ++i) {
            if (prev_ptrs[i]->next_ptrs[i] != ptr) {
                break;
            }
            prev_ptrs[i]->next_ptrs[i] = ptr->next_ptrs[i];
        }
    }

    optional<V> get(const V& key) {
        auto ptr = find_ptr(key);
        if (ptr != nullptr) {
            return ptr->value;
        }
        return {};
    }

    int random_level() {
        int level = 1;
        while (distribution(generator) < p && level < max_level) {
            ++level;
        }
        return level;
    }
    friend std::ostream& operator<< (std::ostream& os, const SkipList<K, V>& skip_list) {
        for (int i = skip_list.max_level - 1; i >= 0; --i) {
            auto p = skip_list.head->next_ptrs[i];
            while (p != nullptr) {
                os << p->key << " ";
                p = p->next_ptrs[i];
            }
            os << endl;
        }
        return os;
    }    

private:
    shared_ptr<Node<K, V>> find_ptr(const K& key) {
        auto p = head;
        for (int i = max_level - 1; i >= 0; --i) {
            while (p->next_ptrs[i] != nullptr && p->next_ptrs[i]->key < key) {
                p = p->next_ptrs[i];
            }
            if (p->next_ptrs[i] != nullptr && p->next_ptrs[i]->key == key) {
                return p->next_ptrs[i];
            }
        }
        return nullptr;
    }
    default_random_engine generator;
    uniform_real_distribution<double> distribution;
    shared_ptr<Node<K, V>> head;
    int max_level;
    double p;
};

int main() {
    SkipList<int, int> skiplist(0.5, 4);
    skiplist.set(1, 10);
    
    skiplist.set(3, 30);
    
    skiplist.set(10, 100);
    
    skiplist.set(2, 20);
    cout << skiplist << endl;
    auto val = skiplist.get(1);
    cout << "Query 1:" << endl;
    if (val.has_value()) {
        cout << val.value() << endl;
    }
    skiplist.remove(1);
    cout << skiplist << endl;
    skiplist.remove(3);
    cout << skiplist << endl;
    return 0;
}